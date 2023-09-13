from aws_cdk import (
    # Duration,
    Stack,
    RemovalPolicy,
    aws_s3 as s3,
    aws_cloudfront as cf,
    aws_cloudfront_origins as cfo
    # aws_sqs as sqs,
)
from constructs import Construct
import json

class VueDigiStandStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(self, 'vue-digi-stand-website-bucket',
            bucket_name='vue-digi-stand-website-bucket',
            website_index_document='index.html',
            website_error_document='error.html',
            public_read_access=True,
            removal_policy=RemovalPolicy.DESTROY
        )

        cf_bucket = s3.Bucket(self, 'vue-digi-stand-cf-bucket',
            bucket_name='vue-digi-stand-cf-bucket',
            access_control=s3.BucketAccessControl.PRIVATE
        )

        origin_access_identity = cf.OriginAccessIdentity(self, 'OriginAccessIdentity')
        cf_bucket.grant_read(origin_access_identity)

        distribution = cf.Distribution(self, 'Distribution',
            default_root_object='index.html',
            default_behavior=cf.BehaviorOptions(
                origin=cfo.S3Origin(cf_bucket, 
                    origin_access_identity=origin_access_identity
                )
            ),
            error_responses=[cf.ErrorResponse(
                http_status=h,
                response_http_status=rh,
                response_page_path=rpp) for (h, rh, rpp) in [
                    (403, 200, '/index.html'),
                    (404, 200, '/index.html')
                ]]
        )

        # example resource
        # queue = sqs.Queue(
        #     self, "SocketApiQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
