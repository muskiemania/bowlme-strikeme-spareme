import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';

import Immutable from 'immutable';
import ImmutablePropTypes from 'react-immutable-proptypes';

import { itemsFetchData } from '../../actions/pokerGameActions';

import _ from 'lodash';
import Cards from '../shared/cards/cards';

class PokerHand extends Component {

    componentDidMount() {
        this.props.fetchData('http://localhost:5000/static/mock.js');
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
                        <Cards cards={cards || Immutable.List()} />
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

