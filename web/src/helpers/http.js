import Promise from 'bluebird';

export function post(url, postData) {

    console.log(postData);
    
    return new Promise((resolve, reject) => {
	
	fetch(url,
	      {method: 'POST',
	       headers: {'Content-Type': 'application/json'},
	       data: JSON.stringify(postData) })
    })
	.then((resp) => {
	    return resp.json();
	});

    /*
    return new Promise((resolve, reject) => {
	console.log('inside of promise');
	console.log('url is: ' + url);
	let req = new XmlHttpRequest();
	req.open('POST', url);
	console.log('headers');
	req.setRequestHeader('Content-Type', 'application/json');
	console.log('open POST');
	req.onload = function() {
	    console.log('onload');
	    if(req.status === 200) {
		console.log('status 200');
		console.log(req.response);
		resolve(JSON.parse(req.response));
	    }
	    else {
		console.log('rejected');
		console.log(req.status);
		console.log(req.statusText);
		reject({
		    code: req.status,
		    message: req.statusText
		});
	    }
	    
	};
	console.log('ready to send: ' + data);
	req.send(data);
    });
*/
}
