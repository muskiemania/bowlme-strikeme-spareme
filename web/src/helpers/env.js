
export function getApiPath() {
    //return 'http://bowl-api.muskiemania.net';
    return `${process.env.API_PATH}`
    //return 'http://localhost:5001';
}

export function getWebPath() {
    //return 'http://bowl-www.muskiemania.net';
    return `${process.env.WEB_PATH}`
    //return 'http://localhost:5000';
}
