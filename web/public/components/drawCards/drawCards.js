import React from 'react';
import PropTypes from 'prop-types';
import ImmutablePropTypes from 'react-immutable-proptypes';
import {render} from 'react-dom';

export default class DrawCardsOrDiscard extends React.Component {

    render() {
        let {cardsInHand, canDrawAgain} = this.props;

        let mustDiscard = cardsInHand > 5;

        if(mustDiscard) {
            return (
                <div className='buttons grid-x row'>                    
                    <div className='small-4 column'>&nbsp;</div>
                    <div className='small-4 column'>Discard</div>
                    <div className='small-4 column'>&nbsp;</div>
                </div>
                
            );
        }

        if(canDrawAgain) {
            return (
                <div className='buttons grid-x row'>
                    <div className='small-1 column'>&nbsp;</div>
                    <div className='small-3 column'>Spare</div>
                    <div className='small-3 column'>Strike</div>
                    <div className='small-1 column'>&nbsp;</div>
                    <div className='small-1 column'>+3</div>
                    <div className='small-1 column'>+4</div>
                    <div className='small-1 column'>+6</div>
                    <div className='small-1 column'>&nbsp;</div>
                </div>
            );
        }

        return null;
    };
}

DrawCardsOrDiscard.propTypes = {
    cardsInHand: PropTypes.number,
    canDrawAgain: PropTypes.boolean
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
