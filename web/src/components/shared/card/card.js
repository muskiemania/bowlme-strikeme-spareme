import React, { Component } from 'react';
import PropTypes from 'prop-types';
import {render} from 'react-dom';
import './card.less';
import Cardinality from '../cardinality/cardinality';
import Suit from '../suit/suit';
import classnames from 'classnames';
import Immutable from 'immutable';

import _ from 'lodash';

class Card extends Component {

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

    handleTouchStart(){
        this.props.toggleSelected(this.props.card);
    }
    
    render() {
        let {card, index, isSelected} = this.props;

        return (
            <div className={classnames('column', 'a-card', this.getSuit(card), `card-${index}`, isSelected ? 'selected' : '')} onTouchStart={this.handleTouchStart.bind(this)} onClick={this.handleTouchStart.bind(this)}>
                <Cardinality value={this.getCardinality(card)} />
                <Suit value={this.getSuit(card)} />
                <div className={'big'}>
                    <Suit value={this.getSuit(card)} />
                </div>         
            </div>
        );
    }
}

Card.propTypes = {
    card: PropTypes.string,
    index: PropTypes.number,
    isSelected: PropTypes.bool,
    toggleSelected: PropTypes.func
};

export default Card;
