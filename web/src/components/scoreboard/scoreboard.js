import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import Immutable from 'immutable';
import ImmutablePropTypes from 'react-immutable-proptypes';

import io from 'socket.io-client';

import { pokerGameGetData, pokerGamePostData, resetSession } from '../../actions/pokerGameActions';

import { getApiPath, getWebPath } from '../../helpers/env';

import _ from 'lodash';
import ScoreboardRow from '../shared/scoreboardRow/scoreboardRow';
import Button from '../shared/button/button';

import './scoreboard.less';

class Scoreboard extends Component {

    constructor(props) {
        super(props);
        this.state = { selectedCards: Immutable.List(), joined: false };
    }

    componentDidMount() {

    	this.socket = io('http://localhost:5000');
		
	this.socket.on('table-activity', data => {
	    this.gameOpsFactory('tableActivity', null);
	    console.log('table activity was broadcasted!');
	});

	this.gameOpsFactory('initialLoad', null);
    }
    
    componentWillReceiveProps(nextProps) {

	let key = nextProps && nextProps.game && nextProps.game.get('game') && nextProps.game.get('game').get('key') || '';
	if(!this.state.joined === true && key) {
	    this.socket.emit('join-game', { gameKey: key });
	    this.state.joined = true;
	}
    }

    shouldComponentUpdate(nextProps, nextState) {
	return (nextState && nextState.joined === false) || true;
    }

    handleButtonClick(operation, payload) {
	this.gameOpsFactory(operation, payload);
    }

    gameOpsFactory(operationName, payload) {

	switch(operationName) {
	case 'initialLoad':
	case 'tableActivity':
	    return this.props.operations.get(operationName)(getApiPath() + '/api/results');
	case 'endGame':
	    return this.props.operations.get(operationName)(getApiPath() + '/api/game/end');
	case 'playAgain':
	    this.props.operations.get(operationName)();
	    window.location = '/';
	default:
	    return;
	}
    }
    
    render() {

        let {game, isError, isLoading} = this.props;
	
        if(isError) {
            return (
                <div className='poker-table'>
                    <p>Sorry, an error has occurred</p>
                </div>
            );
        }

        if(isLoading) {
            return (
                <div className='poker-table'>
                    <p>Loading...</p>
                </div>
            );
        }

	let players = Immutable.List();
	if (game && game.get('players')) {
	    players = game.get('players').sortBy(player => {
		if(!player.get('rating')) {
		    return 9999;
		}
		if(!player.get('rating').get('rank')) {
		    return 9999;
		}
		return player.get('rating').get('rank');
	    });
	}

	let me = game && game.get('playerId');
	let host = game && game.get('game') && game.get('game').get('hostPlayerId');
	let status = game && game.get('game') && game.get('game').get('status') && game.get('game').get('status').get('statusId');
	
	let isHost = (me === host);
	let isGameFinished = (status === 5);

	let allPlayersFinished = false;

	if(game && game.get('players')) {
	    console.log('x');
	    console.log(game.get('players'));
	    
	    allPlayersFinished = game.get('players').every(player => {
		console.log('y');
		console.log(player);
		return player.get('status').get('statusId') === 4;
	    });
	}
	
        return (
	    <div>
            <div className='scoreboard'>
            {
                players.map((player, i) => {
                    return <ScoreboardRow player={player} key={`player-${i}`} />
                })
            }
	    </div>
            <div className='buttons'>
                <div className='button-overlay'>
		{ (isHost && !allPlayersFinished) ?
                  <Button text='End Game' clickOperation={'endGame'} clickPayload={{}} click={this.handleButtonClick.bind(this)} /> : ''
		}
	    { isGameFinished ?
	      <Button text='Game Is Over' clickOperation={'playAgain'} clickPayload={{}} click={this.handleButtonClick.bind(this)} /> : ''
	    }
	    {
		isGameFinished ?
		    <Button text='Play Again' clickOperation={'playAgain'} clickPayload={{}} click={this.handleButtonClick.bind(this)} /> : ''
	    }
                </div>
		</div>
            </div>
        );        
    }
}

Scoreboard.propTypes = {
    operations: ImmutablePropTypes.map.isRequired,
    game: ImmutablePropTypes.map,
    isError: PropTypes.bool.isRequired,
    isLoading: PropTypes.bool.isRequired
};

const mapStateToProps = (state) => {
    return {
        game: state.game,
        isError: state.isError,
        isLoading: state.isLoading
    };
};

const mapDispatchToProps = (dispatch) => {
    let operations = Immutable.Map();
    operations = operations.set('initialLoad', (url) => dispatch(pokerGameGetData(url)));
    operations = operations.set('tableActivity', (url) => dispatch(pokerGameGetData(url)));
    operations = operations.set('endGame', (url) => dispatch(pokerGamePostData(url, {})));
    operations = operations.set('playAgain', () => dispatch(resetSession()));
    
    return {
	operations: operations
    };
};

export default connect(mapStateToProps, mapDispatchToProps)(Scoreboard);
