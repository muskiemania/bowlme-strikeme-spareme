import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';

import Immutable from 'immutable';
import ImmutablePropTypes from 'react-immutable-proptypes';
import _ from 'lodash';

import io from 'socket.io-client';

import { pokerGameGetData, pokerGamePostData } from '../../actions/pokerGameActions';
import { getApiPath, getWebPath } from '../../helpers/env';

import Seats from '../../components/seats/seats';
import PokerHand from '../../components/pokerHand/pokerHand';
import DrawCards from '../../components/drawCards/drawCards';
import Pregame from '../../components/pregame/pregame';

import './pokerGame.less';

class PokerGame extends Component {

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
    
    getSelectedCards() {
        return this.state.selectedCards;
    }

    gameOpsFactory(operationName, payload) {

	let key = this.props.game && this.props.game.get('game') && this.props.game.get('game').get('key') || '';

	switch(operationName) {
	case 'initialLoad':
	case 'tableActivity':
	    return this.props.operations.get(operationName)(getApiPath() + '/api/game');
	case 'startGame':
	    let started = this.props.operations.get(operationName)(getApiPath() + '/api/game/start');
	    key && this.socket.on(key).emit('table-activity');
	    return started;
	case 'drawCards':
	    let drawn = this.props.operations.get(operationName)(getApiPath() + '/api/game/draw', payload);
	    key && this.socket.on(key).emit('table-activity');
	    return drawn;
	case 'discardCards':
	    let discarded = this.props.operations.get(operationName)(getApiPath() + '/api/game/discard', {'cards': this.getSelectedCards()});
	    key && this.socket.on(key).emit('table-activity');
	    return discarded;
	case 'finishGame':
	    let response = this.props.operations.get(operationName)(getApiPath() + '/api/game/finish');
	    console.log(response);
	    //window.location.href = '/results/';
	default:
	    return;
	}
    }
    
    handleButtonClick(operation, payload) {
	this.gameOpsFactory(operation, payload);
    }

    toggleCard(card) {
        let selectedCards = this.state.selectedCards;
        if(selectedCards.contains(card)) {
            selectedCards = selectedCards.filter(c => c != card);
        }
        else {
            selectedCards = selectedCards.push(card);
        }

        this.setState({ selectedCards: selectedCards });
    }

    drawButtonFactory(game, player, numOthers) {
	let gameStatus = game.get('status') || Immutable.Map();
	let hostPlayerId = game.get('hostPlayerId') || '';
	let playerId = player.get('playerId') || '';
	let playerStatus = player.get('status') || Immutable.Map();
	
	let hand = player.get('hand') || Immutable.Map();
	
	if(gameStatus.get('statusId') === 1) {
	    return <Pregame isHost={hostPlayerId === playerId} numberOfPlayers={numOthers} playersRequired={1} click={this.handleButtonClick.bind(this)} />
	}

	if(playerStatus.get('statusId') === 4) {
	    //window.location.href = '/results/';
	    //return;
	}
	
	return (<DrawCards cardsInHand={hand.get('numberOfCards')} cardsSelected={this.getSelectedCards().size} canDrawAgain={ _.includes([1,2], playerStatus.get('statusId') || 0)} click={this.handleButtonClick.bind(this)} />);
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

	let player = game.get('player') || Immutable.Map();
	let others = game.get('otherPlayers') || Immutable.List();
	let gameObj = game.get('game') || Immutable.Map();
	let hand = player.get('hand') || Immutable.Map();
	
        return (
		<div>
                <div>
		<span id="game-id">{(gameObj.get('key') || '').toUpperCase()}</span>
                <Seats players={others} />
                <PokerHand cards={hand.get('cards')} selected={this.getSelectedCards()} toggleSelected={this.toggleCard.bind(this)} />                
                </div>
		{
		    this.drawButtonFactory(gameObj, player, others.size)
		}
            </div>
        );
    }
}

PokerGame.propTypes = {
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
    operations = operations.set('startGame', (url) => dispatch(pokerGamePostData(url)));
    operations = operations.set('drawCards', (url, numberOfCards) => dispatch(pokerGamePostData(url, numberOfCards)));
    operations = operations.set('discardCards', (url, cardsToDiscard) => dispatch(pokerGamePostData(url, cardsToDiscard)));
    operations = operations.set('finishGame', (url) => dispatch(pokerGamePostData(url, {})));
    
    return {
	operations: operations
    };
};

export default connect(mapStateToProps, mapDispatchToProps)(PokerGame);
