import Promise from 'bluebird';
import cookie from 'react-cookies';
const bowlCookie = 'X-Bowl-Token';

function getCookie(key) {
    return cookie.load(key);
}

function setCookie(key, value) {
    const maxAge = 2700;
    cookie.save(key, value, { path: '/', maxAge });
}

//uses:
//
// need to check for cookie in order to get jwt
// get - on entry to join and create in case they are returning to an active game
// post- all non-join actions
// post- join actions are free, and they will return jwt and store cookie

export function postAnonymous(url, data) {
    return Promise.resolve(post(url, data))
	.then((resp) => {
	    setCookie(bowlCookie, resp.jwt);
	    return resp;
	});
}

export function get(url) {
    return Promise.resolve(fetch(url, {
	method: 'GET',
	headers: {
	    'Accept': 'application/json',
	    'Content-Type': 'application/json',
	    'X-Bowl-Token': getCookie(bowlCookie)
	}}))
	.then((resp) => {
	    return resp.json();
	});
}

export function post(url, postData) {

    return Promise.resolve(fetch(url, {
	method: 'POST',
	headers: {
	    'Accept': 'application/json',
	    'Content-Type': 'application/json',
	    'X-Bowl-Token': getCookie(bowlCookie)
	},
	body: JSON.stringify(postData) }))
	.then((resp) => {
	    return resp.json();
	});
}
