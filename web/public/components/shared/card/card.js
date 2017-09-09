import React from 'react';
import PropTypes from 'prop-types';
import {render} from 'react-dom';
import './card.less';
import Cardinality from '../cardinality/cardinality';
import Suit from '../suit/suit';
import classnames from 'classnames';

import _ from 'lodash';

class Card extends React.Component {

    getSuit(card) {

        let suit = card.charAt(1);

        let suits = {};
        suits['C'] = 'clubs';
        suits['D'] = 'diamonds';
        suits['H'] = 'hearts';
        suits['S'] = 'spades';
        
        if(suit in suits){
            return suits[suit];
        }

        return '';
    }

    getCardinality(card) {

        return card.charAt(0);
    }
    
    render() {
        let {card, isLast} = this.props;

        return (
            <div className={classnames('column', 'a-card', this.getSuit(card), isLast ? 'last-card' : '')}>
                <Cardinality value={this.getCardinality(card)} />
                <Suit value={this.getSuit(card)} />
                <div className={isLast ? 'big' : 'reg'}>
                    <Suit value={this.getSuit(card)} />
                </div>         
            </div>
        );
    }
}

Card.propTypes = {
    card: PropTypes.string,
    isLast: PropTypes.bool
};

export default Card;
