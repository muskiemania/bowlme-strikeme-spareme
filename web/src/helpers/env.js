import dotenv from 'dotenv';

dotenv.config();

export function getApiPath() {
    //return 'http://bowl-api.muskiemania.net';
    return `${API_PATH}`
    //return 'http://localhost:5001';
}

export function getWebPath() {
    //return 'http://bowl-www.muskiemania.net';
    return `${WEB_PATH}`
    //return 'http://localhost:5000';
}
