import React, { Component } from 'react';
import PropTypes from 'prop-types';
import ImmutablePropTypes from 'react-immutable-proptypes';

import './drawCards.less';

import Button from '../shared/button/button';

export default class DrawCards extends Component {

    render() {
        let {cardsInHand, canDrawAgain} = this.props;

        //let mustDiscard = cardsInHand > 5;
        let mustDiscard = false;
        
        if(mustDiscard) {
            return (
                <div className='draw-cards grid-x row'>                    
                    <div className='small-4 column'>&nbsp;</div>
                    <div className='small-4 column text-center'>
                        <Button text='Discard' />
                    </div>
                    <div className='small-4 column'>&nbsp;</div>
                </div>
                
            );
        }

        if(canDrawAgain) {
            return (
                <div className='draw-cards grid-x row'>
                    <div className='small-1'>&nbsp;</div>
                    <div className='small-3 column text-center'>
                        <Button text='Spare' />
                    </div>
                    <div className='small-3 column text-center'>
                        <Button text='Strike' />
                    </div>
                    <div className='small-4 column text-center'>
                        <ul className='button-group draw-button-group'>
                            <li><a className='small button'>+3</a></li>
                            <li><a className='small button'>+4</a></li>
                            <li><a className='small button'>+6</a></li>
                            <li><a className='small button'>Finish</a></li>
                        </ul>
                    </div>
                    <div className='small-1'>&nbsp;</div>
                </div>
            );
        }

        return null;
    };
}

DrawCards.propTypes = {
    cardsInHand: PropTypes.number,
    canDrawAgain: PropTypes.bool
};

/*
   draw options: draw 1, draw 2, +3, +4, +
   
   after a draw 1, if number of cards > 5 must discard until number of cards reaches 5
   then all draw options return

   after a draw 2, if the number of cards > 5 must discard until number of cards reaches 5
   then all draw options return

   after a +3, +4, +6, if number of cards > 5 must discard until number of cards reaches 5
   then no more drawing is allowed
*/
