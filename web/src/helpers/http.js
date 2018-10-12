import Promise from 'bluebird';
import cookie from 'react-cookies';
const bowlCookie = 'X-Bowl-Token';

function getCookie(key) {
    return cookie.load(key);
}

function setCookie(key, value) {
    const maxAge = 4800;
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
	.then(response => {
	    setCookie(bowlCookie, response.jwt);
	    return response;
	});
}

export function clearCookie() {
    cookie.remove(bowlCookie, { path: '/' });
}

export function get(url) {
    let request = {
	method: 'GET',
	headers: {
	    'Accept': 'application/json',
	    'Content-Type': 'application/json',
	    'X-Bowl-Token': getCookie(bowlCookie)
	}
    };
    
    return fetch(url, request)
	.then(response => {
	    if(response.ok) {
		return response.json()
		    .then(json => {
			console.log(json);
			return json.body;
		    });
	    }
	    return response.json().then(error => ({error}));
	});			       
}

export function post(url, postData) {

    let request = {
	method: 'POST',
	headers: {
	    'Accept': 'application/json',
	    'Content-Type': 'application/json',
	    'X-Bowl-Token': getCookie(bowlCookie)
	},
	body: JSON.stringify(postData)
    };
    
    return fetch(url, request)
	.then(response => {
	    if(response.ok) {
		return response.json()
		    .then(json => {
			console.log(json);
			return json.body;
		    });
	    }
	    return response.json().then(error => ({error}));
	});
}
