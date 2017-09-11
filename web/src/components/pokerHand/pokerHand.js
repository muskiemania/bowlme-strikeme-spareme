import React, { Component } from 'react';
import PropTypes from 'prop-types';

import Immutable from 'immutable';
import ImmutablePropTypes from 'react-immutable-proptypes';

import './pokerHand.less';
import Cards from '../shared/cards/cards';

class PokerHand extends Component {

    render() {
        let {cards, selected, toggleSelected} = this.props;
        
        return (
            <div className='grid-x row'>
                <div className='small-12 columns'>
                    <div className='grid-x row align-center'>
                        <Cards cards={cards || Immutable.List()} selected={selected} toggleSelected={toggleSelected} />
                    </div>
                </div>
            </div>
        );
    }
}

PokerHand.propTypes = {
    cards: ImmutablePropTypes.list,
    selected: ImmutablePropTypes.list,
    toggleSelected: PropTypes.func
};

export default PokerHand;

