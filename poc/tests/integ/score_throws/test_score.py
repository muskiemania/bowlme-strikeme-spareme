import boto3
from boto3.dynamodb.types import TypeDeserializer
import copy
import json
import os
import pytest
import random

class Test_ScoreThrows:

    _FUNCTION_THROW = None
    _FUNCTION_SCORE = None
    _TABLE_NAME = None
    _TEST_SERIES_ID = None
    _TEST_GAME_NUMBER = None
    _DYNAMO_CLIENT = None
    _LAMBDA_CLIENT = None

    @pytest.fixture(scope='session', autouse=True)
    def before_all(self):
        Test_ScoreThrows._FUNCTION_THROW = os.environ['CREATE_THROW_FUNCTION_NAME']
        Test_ScoreThrows._FUNCTION_SCORE = os.environ['SCORE_THROWS_FUNCTION_NAME']
        Test_ScoreThrows._TABLE_NAME = os.environ['BOWLING_TRAINER_TABLE_NAME']
        Test_ScoreThrows._TEST_SERIES_ID = 'test123'
        Test_ScoreThrows._TEST_GAME_NUMBER = 1

        Test_ScoreThrows._DYNAMO_CLIENT = boto3.client('dynamodb')
        Test_ScoreThrows._LAMBDA_CLIENT = boto3.client('lambda')

        print('setup')
        print(self._TABLE_NAME)

    def try_delete(self):

        print(self._TABLE_NAME)

        # try delete
        try:
            self._DYNAMO_CLIENT.delete_item(
                TableName=self._TABLE_NAME,
                Key={
                    'series_id': {
                        'S': self._TEST_SERIES_ID
                    },
                    'game_number': {
                        'N': str(self._TEST_GAME_NUMBER)
                    }
                }
            )
        except:
            pass


    def test_strike_strike_strike_30(self):
        
        # arrange
        self.try_delete()

        _throw = {
            'series_id': self._TEST_SERIES_ID,
            'game_number': self._TEST_GAME_NUMBER,
            'throw': 'X'
        }

        _input = copy.deepcopy(_throw)
        del _input['throw']

        lambda_ = boto3.client('lambda')
        
        for _ in range(3):

            reply = lambda_.invoke(
                FunctionName=self._FUNCTION_THROW,
                InvocationType='RequestResponse',
                Payload=json.dumps(_throw)
            )

        # act
        reply = lambda_.invoke(
            FunctionName=self._FUNCTION_SCORE,
            InvocationType='RequestResponse',
            Payload=json.dumps(_input)
        )

        # assert - prep
        db = boto3.client('dynamodb')
        item = db.get_item(
            TableName=self._TABLE_NAME,
            Key={
                'series_id': {
                    'S': self._TEST_SERIES_ID
                },
                'game_number': {
                    'N': str(self._TEST_GAME_NUMBER)
                }
            },
            ConsistentRead=True
        )
        
        print('item is:')
        print(item)

        dez = TypeDeserializer()
        item = { 
                k: dez.deserialize(v) for k, v in item['Item'].items()
        }

        

        # assert
        #assert 'best_possible' in item
        assert 'frames' in item
        assert 'total' in item

        assert len(item['frames']) == 3
        assert item['frames'][0]['frame'] == 1
        assert item['frames'][0]['pins'] == 30
        assert item['frames'][0]['total'] == 30
        assert len(item['frames'][0]['throws']) == 1
        assert item['frames'][0]['throws'][0]['pins'] == 'X'
        assert item['total'] == 30

    def test_strike_spare_20(self):
        
        # arrange
        self.try_delete()

        _throws = [
            {
                'series_id': self._TEST_SERIES_ID,
                'game_number': self._TEST_GAME_NUMBER,
                'throw': 'X'
            },
            {
                'series_id': self._TEST_SERIES_ID,
                'game_number': self._TEST_GAME_NUMBER,
                'throw': random.choice([0,1,2,3,4,5,6,7,8,9])
            },
            {
                'series_id': self._TEST_SERIES_ID,
                'game_number': self._TEST_GAME_NUMBER,
                'throw': '/'
            },
            
        ]

        _input = copy.deepcopy(_throws[0])
        del _input['throw']

        lambda_ = boto3.client('lambda')
        
        for t in _throws:

            reply = lambda_.invoke(
                FunctionName=self._FUNCTION_THROW,
                InvocationType='RequestResponse',
                Payload=json.dumps(t)
            )

        # act
        reply = lambda_.invoke(
            FunctionName=self._FUNCTION_SCORE,
            InvocationType='RequestResponse',
            Payload=json.dumps(_input)
        )

        # assert - prep
        db = boto3.client('dynamodb')
        item = db.get_item(
            TableName=self._TABLE_NAME,
            Key={
                'series_id': {
                    'S': self._TEST_SERIES_ID
                },
                'game_number': {
                    'N': str(self._TEST_GAME_NUMBER)
                }
            },
            ConsistentRead=True
        )
        
        print('item is:')
        print(item)

        dez = TypeDeserializer()
        item = { 
                k: dez.deserialize(v) for k, v in item['Item'].items()
        }

        # assert
        #assert 'best_possible' in item
        assert 'frames' in item
        assert 'total' in item

        assert len(item['frames']) == 2
        assert item['frames'][0]['frame'] == 1
        assert item['frames'][0]['pins'] == 20
        assert item['frames'][0]['total'] == 20
        assert len(item['frames'][0]['throws']) == 1
        assert item['frames'][0]['throws'][0]['pins'] == 'X'
        assert item['total'] == 20

    def test_strike_open(self):
        
        # arrange
        self.try_delete()

        _throws = [
            {
                'series_id': self._TEST_SERIES_ID,
                'game_number': self._TEST_GAME_NUMBER,
                'throw': 'X'
            },
            {
                'series_id': self._TEST_SERIES_ID,
                'game_number': self._TEST_GAME_NUMBER,
                'throw': random.choice([0,1,2,3,4])
            },
            {
                'series_id': self._TEST_SERIES_ID,
                'game_number': self._TEST_GAME_NUMBER,
                'throw': random.choice([0,1,2,3,4])
            },
            
        ]

        _input = copy.deepcopy(_throws[0])
        del _input['throw']

        lambda_ = boto3.client('lambda')
        
        for t in _throws:

            reply = lambda_.invoke(
                FunctionName=self._FUNCTION_THROW,
                InvocationType='RequestResponse',
                Payload=json.dumps(t)
            )

        # act
        reply = lambda_.invoke(
            FunctionName=self._FUNCTION_SCORE,
            InvocationType='RequestResponse',
            Payload=json.dumps(_input)
        )

        # assert - prep
        db = boto3.client('dynamodb')
        item = db.get_item(
            TableName=self._TABLE_NAME,
            Key={
                'series_id': {
                    'S': self._TEST_SERIES_ID
                },
                'game_number': {
                    'N': str(self._TEST_GAME_NUMBER)
                }
            },
            ConsistentRead=True
        )
        
        print('item is:')
        print(item)

        dez = TypeDeserializer()
        item = { 
                k: dez.deserialize(v) for k, v in item['Item'].items()
        }

        # assert
        #assert 'best_possible' in item
        assert 'frames' in item
        assert 'total' in item

        assert len(item['frames']) == 2
        assert item['frames'][0]['frame'] == 1
        assert item['frames'][0]['pins'] == 10 + _throws[1]['throw'] + _throws[2]['throw']
        assert item['frames'][0]['total'] == 10 + _throws[1]['throw'] + _throws[2]['throw']
        assert len(item['frames'][0]['throws']) == 1
        assert item['frames'][0]['throws'][0]['pins'] == 'X'
        assert item['total'] == 10 + (2 * (_throws[1]['throw'] + _throws[2]['throw']))

    def test_spare_zero(self):
        
        # arrange
        self.try_delete()

        _throws = [
            {
                'series_id': self._TEST_SERIES_ID,
                'game_number': self._TEST_GAME_NUMBER,
                'throw': random.choice([0,1,2,3,4,5,6,7,8,9])
            },
            {
                'series_id': self._TEST_SERIES_ID,
                'game_number': self._TEST_GAME_NUMBER,
                'throw': '/'
            },
            {
                'series_id': self._TEST_SERIES_ID,
                'game_number': self._TEST_GAME_NUMBER,
                'throw': 0
            },
            
        ]

        _input = copy.deepcopy(_throws[0])
        del _input['throw']

        lambda_ = boto3.client('lambda')
        
        for t in _throws:

            reply = lambda_.invoke(
                FunctionName=self._FUNCTION_THROW,
                InvocationType='RequestResponse',
                Payload=json.dumps(t)
            )

        # act
        reply = lambda_.invoke(
            FunctionName=self._FUNCTION_SCORE,
            InvocationType='RequestResponse',
            Payload=json.dumps(_input)
        )

        # assert - prep
        db = boto3.client('dynamodb')
        item = db.get_item(
            TableName=self._TABLE_NAME,
            Key={
                'series_id': {
                    'S': self._TEST_SERIES_ID
                },
                'game_number': {
                    'N': str(self._TEST_GAME_NUMBER)
                }
            },
            ConsistentRead=True
        )
        
        print('item is:')
        print(item)

        dez = TypeDeserializer()
        item = { 
                k: dez.deserialize(v) for k, v in item['Item'].items()
        }

        # assert
        #assert 'best_possible' in item
        assert 'frames' in item
        assert 'total' in item

        assert len(item['frames']) == 2
        assert item['frames'][0]['frame'] == 1
        assert item['frames'][0]['pins'] == 10 + _throws[2]['throw']
        assert item['frames'][0]['total'] == 10 + _throws[2]['throw']
        assert len(item['frames'][0]['throws']) == 2
        assert item['frames'][0]['throws'][0]['pins'] == _throws[0]['throw']
        assert item['frames'][0]['throws'][1]['pins'] == '/'
        assert item['total'] == 10

    def test_spare_open(self):
        
        # arrange
        self.try_delete()

        _throws = [
            {
                'series_id': self._TEST_SERIES_ID,
                'game_number': self._TEST_GAME_NUMBER,
                'throw': random.choice([0,1,2,3,4,5,6,7,8,9])
            },
            {
                'series_id': self._TEST_SERIES_ID,
                'game_number': self._TEST_GAME_NUMBER,
                'throw': '/'
            },
            {
                'series_id': self._TEST_SERIES_ID,
                'game_number': self._TEST_GAME_NUMBER,
                'throw': random.choice([1,2,3,4,5,6,7,8,9])
            },
            
        ]

        _input = copy.deepcopy(_throws[0])
        del _input['throw']

        lambda_ = boto3.client('lambda')
        
        for t in _throws:

            reply = lambda_.invoke(
                FunctionName=self._FUNCTION_THROW,
                InvocationType='RequestResponse',
                Payload=json.dumps(t)
            )

        # act
        reply = lambda_.invoke(
            FunctionName=self._FUNCTION_SCORE,
            InvocationType='RequestResponse',
            Payload=json.dumps(_input)
        )

        # assert - prep
        db = boto3.client('dynamodb')
        item = db.get_item(
            TableName=self._TABLE_NAME,
            Key={
                'series_id': {
                    'S': self._TEST_SERIES_ID
                },
                'game_number': {
                    'N': str(self._TEST_GAME_NUMBER)
                }
            },
            ConsistentRead=True
        )
        
        print('item is:')
        print(item)

        dez = TypeDeserializer()
        item = { 
                k: dez.deserialize(v) for k, v in item['Item'].items()
        }

        # assert
        #assert 'best_possible' in item
        assert 'frames' in item
        assert 'total' in item

        assert len(item['frames']) == 2
        assert item['frames'][0]['frame'] == 1
        assert item['frames'][0]['pins'] == 10 + _throws[2]['throw']
        assert item['frames'][0]['total'] == 10 + _throws[2]['throw']
        assert len(item['frames'][0]['throws']) == 2
        assert item['frames'][0]['throws'][0]['pins'] == _throws[0]['throw']
        assert item['frames'][0]['throws'][1]['pins'] == '/'
        assert item['total'] == 10 + (2 * _throws[2]['throw'])

