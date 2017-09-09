
import React from 'react';
import PropTypes from 'prop-types';
import ImmutablePropTypes from 'react-immutable-proptypes';
import {render} from 'react-dom';
import './cards.less';
import _ from 'lodash';
import Card from '../card/card';

const Cards = ((props) => {

    let {cards} = props;

    let firstCards = cards.pop();
    let lastCard = cards.last();
    
    return (
        <div className='cards-collection grid-x row'>
            {
                cards.size > 1 ? cards.pop().map((card, i) => { return <Card card={card} key={i} />}) : null
            }
            {
                cards.size > 0 ? <Card card={cards.last()} isLast={true} /> : null
            }
        </div>
    );
});

Cards.propTypes = {
    cards: ImmutablePropTypes.list
};

export default Cards;

