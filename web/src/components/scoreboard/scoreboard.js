import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import Immutable from 'immutable';
import ImmutablePropTypes from 'react-immutable-proptypes';

import io from 'socket.io-client';

import { pokerGameGetData, pokerGamePostData } from '../../actions/pokerGameActions';
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

    gameOpsFactory(operationName, payload) {

	switch(operationName) {
	case 'initialLoad':
	case 'tableActivity':
	    return this.props.operations.get(operationName)(getApiPath() + '/api/results');
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
	if (game.get('players')) {
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

	let isHost = false;
	let isGameFinished = false;
	
	
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
		{ (isHost && !isGameFinished) ?
                  <Button text='End Game' clickOperation={'endGame'} clickPayload={{'numberOfCards': 1}} click={this.props.click} /> : ''
		}
	    { isGameFinished ?
	      <Button text='Game Is Over' clickOperation={'gameOver'} clickPayload={{'numberOfCards': 2}} click={this.props.click} /> : ''
	    }
	    { isGameFinished ?
	      <Button text='Play Again' clickOperation={'playAgain'} clickPayload={{'numberOfCards': 2}} click={this.props.click} /> : ''
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
    
    return {
	operations: operations
    };
};

export default connect(mapStateToProps, mapDispatchToProps)(Scoreboard);
