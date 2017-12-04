import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import Immutable from 'immutable';
import ImmutablePropTypes from 'react-immutable-proptypes';

import { pokerGameGetData, pokerGamePostData } from '../../actions/pokerGameActions';
import { getApiPath, getWebPath } from '../../helpers/env';

import _ from 'lodash';
import ScoreboardRow from '../shared/scoreboardRow/scoreboardRow';

import './scoreboard.less';

class Scoreboard extends Component {

    constructor(props) {
        super(props);

        this.state = { selectedCards: Immutable.List() };
    }

    componentDidMount() {
	this.gameOpsFactory('initialLoad', null);
    }
    
    gameOpsFactory(operationName, payload) {

	switch(operationName) {
	case 'initialLoad':
	    return this.props.operations.get(operationName)(getApiPath() + '/api/results');
	//case 'startGame':
	//    return this.props.operations.get(operationName)('http://127.0.0.1:5001/api/game/start');
	//case 'drawCards':
	//    return this.props.operations.get(operationName)('http://127.0.0.1:5001/api/game/draw', payload);
	//case 'discardCards':
	//    return this.props.operations.get(operationName)('http://127.0.0.1:5001/api/game/discard', {'cards': this.getSelectedCards()});
	//case 'finishGame':
	//    return this.props.operations.get(operationName)('http://127.0.0.1:5001/api/game/finish');
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

        
        //let players = Immutable.fromJS([
        //    { playerName: 'Justin', rating: { rank: 3, description: '' } },
        //    { playerName: 'Sarah', cards: ['2H','4H','6H','8H','JH'], rating: { rank: 2, description: 'Flush' } },
        //    { playerName: 'Doofus', rating: { } },
        //    { playerName: 'Jenna', cards: ['KS','KD','KC','KH','7C'], rating: { rank: 1, description: 'Four-Of-A-Kind' } },
	//    { playerName: 'Someone', cards: ['2D'], rating: { rank: 4, description: 'High Card' } }
        //]);

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
	
        return (
            <div className='scoreboard'>
            {
                players.map((player, i) => {
                    return <ScoreboardRow player={player} key={`player-${i}`} />
                })
            }
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
    //operations = operations.set('startGame', (url) => dispatch(pokerGamePostData(url)));
    //operations = operations.set('drawCards', (url, numberOfCards) => dispatch(pokerGamePostData(url, numberOfCards)));
    //operations = operations.set('discardCards', (url, cardsToDiscard) => dispatch(pokerGamePostData(url, cardsToDiscard)));
    //operations = operations.set('finishGame', (url) => dispatch(pokerGamePostData(url)));
    
    return {
	operations: operations
    };
};

export default connect(mapStateToProps, mapDispatchToProps)(Scoreboard);
