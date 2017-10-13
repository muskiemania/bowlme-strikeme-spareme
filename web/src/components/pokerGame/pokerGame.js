import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';

import Immutable from 'immutable';
import ImmutablePropTypes from 'react-immutable-proptypes';

import { pokerGameFetchData } from '../../actions/pokerGameActions';
import { get } from '../../helpers/http';

import _ from 'lodash';
import Seats from '../../components/seats/seats';
import PokerHand from '../../components/pokerHand/pokerHand';
import DrawCards from '../../components/drawCards/drawCards';

import './pokerGame.less';

class PokerGame extends Component {

    constructor(props) {
        super(props);

        this.state = { selectedCards: Immutable.List() };
    }

    componentDidMount() {
        //this.props.fetchData('http://localhost:5000/static/mock.js');
	this.props.fetchData('http://127.0.0.1:5001/api/game');
    }
    
    drawCards(numberOfCards) {
        alert(`will draw ${numberOfCards} cards`);
    }

    discardCards(cards) {
        alert(`will discard ${cards}`);
    }

    getSelectedCards() {
        return this.state.selectedCards;
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
    
    render() {

        let {cards, isError, isLoading} = this.props;
	let game = cards;
	
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
	let gameStatus = game.get('gameStatus') || 0;
	let hand = player.get('hand') || Immutable.Map();
	let playerStatus = player.get('status') || Immutable.Map();
	
        return (
		<div>
                <div>
		<span id="game-id">{'XXXXXC'}</span>
                <Seats players={others} />
                <PokerHand cards={hand.get('cards')} selected={this.getSelectedCards()} toggleSelected={this.toggleCard.bind(this)} />                
                </div>
                <DrawCards cardsInHand={hand.get('numberOfCards')} cardsSelected={this.getSelectedCards().size} canDrawAgain={ _.includes([1,2], playerStatus.get('statusId') || 0)} />
            </div>
        );
    }
}

PokerGame.propTypes = {
    fetchData: PropTypes.func.isRequired,
    cards: ImmutablePropTypes.map,
    isError: PropTypes.bool.isRequired,
    isLoading: PropTypes.bool.isRequired
};

const mapStateToProps = (state) => {
    return {
        cards: state.cards,
        isError: state.isError,
        isLoading: state.isLoading
    };
};

const mapDispatchToProps = (dispatch) => {
    return {
        fetchData: (url) => dispatch(get(url))
    };
};

export default connect(mapStateToProps, mapDispatchToProps)(PokerGame);
