import React from 'react';
import PropTypes from 'prop-types';
import Immutable from 'immutable';
import ImmutablePropTypes from 'react-immutable-proptypes';
import {render} from 'react-dom';
import _ from 'lodash';
import Cards from '../shared/cards/cards';

const PokerHand = ((props) => {

    let {cards} = props;

    return (
        <div className='grid-x row'>
            <div className='small-12 columns'>
                <div className='grid-x row align-center'>
                    <Cards cards={cards || Immutable.List()} />
                </div>
            </div>
        </div>
    );
});

PokerHand.propTypes = {
    cards: ImmutablePropTypes.list
};

export default PokerHand;

