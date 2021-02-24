import configparser

from pathlib import Path
import logging
import os

from dotenv import load_dotenv

logger = logging.getLogger(__file__)


def get_env_dict(env_path):
    env_dict = {}
    try:
        load_dotenv(env_path)
    except Exception as e:
        logger.info(f"envファイル読み込みエラー: {e}")
        return

    # 以下に、.envファイルから読み込むパラメータを取得。

    try:
        # Account ID
        env_dict['account_id'] = os.getenv('account_id')
    except ImportError as e:
        logger.info(f"account_idエラー: {e}")

    try:
        # API Key
        env_dict['api_key'] = os.getenv('api_key')
    except ImportError as e:
        logger.info(f"api_keyエラー: {e}")

    try:
        # Access Token
        env_dict['access_token'] = os.getenv('access_token')
    except ImportError as e:
        logger.info(f"access_tokenエラー: {e}")

    try:
        # Account Key
        env_dict['access_key'] = os.getenv('access_key')
    except ImportError as e:
        logger.info(f"access_keyエラー: {e}")

    return env_dict


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent

env_path = BASE_DIR / '.env'
env_dict = get_env_dict(env_path)

config = configparser.ConfigParser()
config.read('config.ini', encoding='UTF-8')

account_id = env_dict['account_id']
api_key = env_dict['api_key']
access_token = env_dict['access_token']
access_key = env_dict['access_key']

key_word = config['twitter']['key_word']
count = int(config['twitter']['count'])
