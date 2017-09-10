
import React from 'react';
import PropTypes from 'prop-types';
import ImmutablePropTypes from 'react-immutable-proptypes';
import {render} from 'react-dom';
import './cards.less';
import _ from 'lodash';
import Card from '../card/card';

const Cards = ((props) => {

    let {cards} = props;

    return (
        <div className='cards-collection grid-x row'>
            {
                cards.size > 0 ? cards.map((card, i) => { return <Card card={card} index={ i+1 } key={`card-${i}`} />}) : null
            }
        </div>
    );
});

Cards.propTypes = {
    cards: ImmutablePropTypes.list
};

export default Cards;

