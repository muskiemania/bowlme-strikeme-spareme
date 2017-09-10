import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';

import Immutable from 'immutable';
import ImmutablePropTypes from 'react-immutable-proptypes';

import { itemsFetchData } from '../../actions/pokerGameActions';

import _ from 'lodash';
import './pokerHand.less';
import Cards from '../shared/cards/cards';

class PokerHand extends Component {

    constructor(props) {
        super(props);

        this.state  = { selected: Immutable.List() };
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
        return this.state.selected;
    }

    toggleCardSelected(card) {
        let selected = this.state.selected;

        if(selected.contains(card)) {
            selected = selected.filter(c => c != card);
        }
        else {
            selected = selected.push(card);
        }
        
        this.setState({ selected: selected });
    }
    
    render() {
        let {cards, hasErrored, isLoading, items} = this.props;
        
        if(hasErrored) {
            return (<p>Sorry! Error has occurred!</p>);
        }
        
        if(isLoading) {
            return (<p>Loading...</p>);
        }
        
        return (
            <div className='grid-x row'>
                <div className='small-12 columns'>
                    <div className='grid-x row align-center'>
                        <Cards cards={cards || Immutable.List()} selected={this.getSelectedCards()} toggleSelected={this.toggleCardSelected.bind(this)} />
                    </div>
                </div>
            </div>
        );
    }
}

PokerHand.propTypes = {
    fetchData: PropTypes.func.isRequired,
    cards: ImmutablePropTypes.list,
    hasErrored: PropTypes.bool.isRequired,
    isLoading: PropTypes.bool.isRequired
};

const mapStateToProps = (state) => {

    console.log('state is: ' + JSON.stringify(state));
    
    return {
        cards: state.cards,
        hasErrored: state.itemsHasErrored,
        isLoading: state.itemsIsLoading
    };
};

const mapDispatchToProps = (dispatch) => {
    return {
        fetchData: (url) => dispatch(itemsFetchData(url))
    };
};

export default connect(mapStateToProps, mapDispatchToProps)(PokerHand);

