import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';

import Immutable from 'immutable';
import ImmutablePropTypes from 'react-immutable-proptypes';

import { pokerGameFetchData } from '../../actions/pokerGameActions';

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
        this.props.fetchData('http://localhost:5000/static/mock.js');
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
        
        return (
		<div>
                <div>
		<span id="game-id">{'X0X0X0'}</span>
                    <Seats players={Immutable.fromJS([
                            {name: 'SARAH', cards:[1,2,3,4]},
                            {name: 'JUSTIN', cards:[]},
                            {name: 'PAUL', cards:[1,2,3]},
                            {name: 'SARA', cards:[1,2,3,4,5,6]},
                            {name: 'JENNA', cards:[1,2,3,4,5], finished: true},
                            {name: 'NEWBABY', cards:[1,2,3,4,5,6,7,8,9,10,11]}
                    ])} />
                    
                    <PokerHand cards={cards} selected={this.getSelectedCards()} toggleSelected={this.toggleCard.bind(this)} />                    
                </div>
                <DrawCards cardsInHand={cards.size} cardsSelected={this.getSelectedCards().size} canDrawAgain={true} />
            </div>
        );
    }
}

PokerGame.propTypes = {
    fetchData: PropTypes.func.isRequired,
    cards: ImmutablePropTypes.list,
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
        fetchData: (url) => dispatch(pokerGameFetchData(url))
    };
};

export default connect(mapStateToProps, mapDispatchToProps)(PokerGame);
