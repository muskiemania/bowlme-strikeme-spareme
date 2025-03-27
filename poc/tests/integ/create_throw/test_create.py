import boto3
from boto3.dynamodb.types import TypeDeserializer
import json
import os
import pytest
import random

class Test_CreateSingleThrow:

    _FUNCTION_NAME = None
    _TABLE_NAME = None
    _TEST_SERIES_ID = None
    _TEST_GAME_NUMBER = None
    _DYNAMO_CLIENT = None
    _LAMBDA_CLIENT = None

    @pytest.fixture(scope='session', autouse=True)
    def before_all(self):
        Test_CreateSingleThrow._FUNCTION_NAME = os.environ['CREATE_THROW_FUNCTION_NAME']
        Test_CreateSingleThrow._TABLE_NAME = os.environ['BOWLING_TRAINER_TABLE_NAME']
        Test_CreateSingleThrow._TEST_SERIES_ID = 'test123'
        Test_CreateSingleThrow._TEST_GAME_NUMBER = 1

        Test_CreateSingleThrow._DYNAMO_CLIENT = boto3.client('dynamodb')
        Test_CreateSingleThrow._LAMBDA_CLIENT = boto3.client('lambda')

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


    def test_single(self):
    
        # arrange
        self.try_delete()

        _throw = random.choice([0,1,2,3,4,5,6,7,8,9])

        _input = {
            'series_id': self._TEST_SERIES_ID,
            'game_number': self._TEST_GAME_NUMBER,
            'throw': _throw
        }

        # act
        lambda_ = boto3.client('lambda')
        reply = lambda_.invoke(
            FunctionName=self._FUNCTION_NAME,
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
        dez = TypeDeserializer()
        item = { 
                k: dez.deserialize(v) for k, v in item['Item'].items()
        }

        # assert
        assert 'series_id' in item
        assert 'game_number' in item
        assert 'throws' in item
        assert 'throw_data' in item

        assert item.get('series_id') == self._TEST_SERIES_ID
        assert item.get('game_number') == self._TEST_GAME_NUMBER
        assert isinstance(item.get('throws'), list)
        assert isinstance(item.get('throw_data'), dict)

        assert len(item.get('throws')) == 1
        assert len(item.get('throw_data').keys()) == 1

        _THROW_ID = item.get('throws')[0]
        assert _THROW_ID in item.get('throw_data')
        
        assert item.get('throw_data', {}).get(_THROW_ID, {}).get('pins') == str(_throw)

    def test_single_X(self):
    
        # arrange
        self.try_delete()

        _throw = 'X'

        _input = {
            'series_id': self._TEST_SERIES_ID,
            'game_number': self._TEST_GAME_NUMBER,
            'throw': _throw
        }

        # act
        lambda_ = boto3.client('lambda')
        reply = lambda_.invoke(
            FunctionName=self._FUNCTION_NAME,
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
        dez = TypeDeserializer()
        item = { 
                k: dez.deserialize(v) for k, v in item['Item'].items()
        }

        # assert
        assert 'series_id' in item
        assert 'game_number' in item
        assert 'throws' in item
        assert 'throw_data' in item

        assert item.get('series_id') == self._TEST_SERIES_ID
        assert item.get('game_number') == self._TEST_GAME_NUMBER
        assert isinstance(item.get('throws'), list)
        assert isinstance(item.get('throw_data'), dict)

        assert len(item.get('throws')) == 1
        assert len(item.get('throw_data').keys()) == 1

        _THROW_ID = item.get('throws')[0]
        assert _THROW_ID in item.get('throw_data')
        
        assert item.get('throw_data', {}).get(_THROW_ID, {}).get('pins') == str(_throw)

    def test_two_throws_spare(self):
    
        # arrange
        self.try_delete()

        _first_throw = random.choice([1,2,3,4,5,6,7,8,9])
        _second_throw = '/'

        _input_1 = {
            'series_id': self._TEST_SERIES_ID,
            'game_number': self._TEST_GAME_NUMBER,
            'throw': _first_throw
        }
        _input_2 = {
            'series_id': self._TEST_SERIES_ID,
            'game_number': self._TEST_GAME_NUMBER,
            'throw': _second_throw
        }

        # act
        lambda_ = boto3.client('lambda')
        reply = lambda_.invoke(
            FunctionName=self._FUNCTION_NAME,
            InvocationType='RequestResponse',
            Payload=json.dumps(_input_1)
        )
        reply = lambda_.invoke(
            FunctionName=self._FUNCTION_NAME,
            InvocationType='RequestResponse',
            Payload=json.dumps(_input_2)
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
        dez = TypeDeserializer()
        item = { 
                k: dez.deserialize(v) for k, v in item['Item'].items()
        }

        # assert
        assert 'series_id' in item
        assert 'game_number' in item
        assert 'throws' in item
        assert 'throw_data' in item

        assert item.get('series_id') == self._TEST_SERIES_ID
        assert item.get('game_number') == self._TEST_GAME_NUMBER
        assert isinstance(item.get('throws'), list)
        assert isinstance(item.get('throw_data'), dict)

        assert len(item.get('throws')) == 2
        assert len(item.get('throw_data').keys()) == 2

        _FIRST_THROW_ID = item.get('throws')[0]
        assert _FIRST_THROW_ID in item.get('throw_data')
        assert item.get('throw_data', {}).get(_FIRST_THROW_ID, {}).get('pins') == str(_first_throw)

        _SECOND_THROW_ID = item.get('throws')[1]
        assert _SECOND_THROW_ID in item.get('throw_data')
        assert item.get('throw_data', {}).get(_SECOND_THROW_ID, {}).get('pins') == str(_second_throw)

    def test_two_throws_no_spare(self):
    
        # arrange
        self.try_delete()

        _first_throw = random.choice([1,2,3,4,5,6,7,8,9])
        _second_throw = 9 - _first_throw

        _input_1 = {
            'series_id': self._TEST_SERIES_ID,
            'game_number': self._TEST_GAME_NUMBER,
            'throw': _first_throw
        }
        _input_2 = {
            'series_id': self._TEST_SERIES_ID,
            'game_number': self._TEST_GAME_NUMBER,
            'throw': _second_throw
        }

        # act
        lambda_ = boto3.client('lambda')
        reply = lambda_.invoke(
            FunctionName=self._FUNCTION_NAME,
            InvocationType='RequestResponse',
            Payload=json.dumps(_input_1)
        )
        reply = lambda_.invoke(
            FunctionName=self._FUNCTION_NAME,
            InvocationType='RequestResponse',
            Payload=json.dumps(_input_2)
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
        dez = TypeDeserializer()
        item = { 
                k: dez.deserialize(v) for k, v in item['Item'].items()
        }

        # assert
        assert 'series_id' in item
        assert 'game_number' in item
        assert 'throws' in item
        assert 'throw_data' in item

        assert item.get('series_id') == self._TEST_SERIES_ID
        assert item.get('game_number') == self._TEST_GAME_NUMBER
        assert isinstance(item.get('throws'), list)
        assert isinstance(item.get('throw_data'), dict)

        assert len(item.get('throws')) == 2
        assert len(item.get('throw_data').keys()) == 2

        _FIRST_THROW_ID = item.get('throws')[0]
        assert _FIRST_THROW_ID in item.get('throw_data')
        assert item.get('throw_data', {}).get(_FIRST_THROW_ID, {}).get('pins') == str(_first_throw)

        _SECOND_THROW_ID = item.get('throws')[1]
        assert _SECOND_THROW_ID in item.get('throw_data')
        assert item.get('throw_data', {}).get(_SECOND_THROW_ID, {}).get('pins') == str(_second_throw)


