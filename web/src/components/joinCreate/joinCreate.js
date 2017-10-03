import React, { Component } from 'react';

import Immutable from 'immutable';
import ImmutablePropTypes from 'react-immutable-proptypes';

import _ from 'lodash';
import Promise from 'bluebird';

import Button from '../shared/button/button';
import Join from '../shared/join/join';
import Create from '../shared/create/create';
import Welcome from '../shared/welcome/welcome';

import { post, get } from '../../helpers/http';

import './joinCreate.less';

class JoinCreate extends Component {

    constructor(props) {
        super(props);

        this.state = { mode: 'welcome' };
    }

    clickSetModeCreate() {
	console.log('entered create');
	get('http://localhost:5001/api/game/create')
	    .then((respJson) => {
		if(respJson.gameId === 0) {
		    this.setState({ mode: 'create' });
		}
		else if (respJson.gameId > 0) {
		    console.log('ready to redirect');
		    window.location.replace('http://localhost:5000/game/');
		}
		else {
		    throw 'Unable to determine game';
		}
	    })
	    .catch((err) => {
		console.log(err);
	    });
    }

    clickSetModeJoin() {
        this.setState({ mode: 'join' });
    }

    clickCreateGame(playerName) {
	console.log('inside joinCreate.js clickCreateGame');
	post('http://localhost:5001/api/game/create', { 'playerName': playerName})
	    .then((respJson) => {
		console.log('inside then');
		if(respJson.gameId === 0) {
		    throw 'Could not create game';
		}

		window.location.replace('http://localhost:5000/game/');
	    })
	    .catch((err) => {
		//animation to show error message
		console.log(err);
	    });
    }

    clickJoinGame(gameKey, playerName) {
	post('http://localhost:5001/api/game/join', {gameKey, playerName})
	    .then((resp) => {
		if(resp.gameId === 0) {
		    throw 'Could not create game';
		}

		window.location.replace('http://localhost:5000/game/');
	    })
	    .catch((err) => {
		//animation to show error message
	    });	
    }

    factory() {
        switch(this.state.mode) {
            case 'create':
            return (<Create clickCreate={this.clickCreateGame.bind(this)} />);
            case 'join':
            return (<Join clickJoin={this.clickJoinGame.bind(this)} />);
            default:
                return (<Welcome clickCreate={this.clickSetModeCreate.bind(this)} clickJoin={this.clickSetModeJoin.bind(this)} />);
        }
    }

    render() {
        return (
            <div className='join-create'>
                {
                    this.factory()
                }
            </div>
        );
    }
}

export default JoinCreate;
