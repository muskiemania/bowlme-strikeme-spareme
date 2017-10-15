import React, { Component } from 'react';
import PropTypes from 'prop-types';
import ImmutablePropTypes from 'react-immutable-proptypes';

import './drawCards.less';

import ButtonGroup from '../shared/buttonGroup/buttonGroup';
import Button from '../shared/button/button';

export default class DrawCards extends Component {

    render() {
        let {cardsInHand, cardsSelected, canDrawAgain, click} = this.props;

        //let mustDiscard = cardsInHand > 5;
        let mustDiscard = false;
        
        if(mustDiscard) {
            return (
                <div className='draw-cards'>
                    <div className='button-overlay'>
                    <Button text='Discard' disabled={(cardsInHand-cardsSelected) != 5} clickOperation={'discardCards'} clickPayload={cardsSelected} click={this.props.click} />
                    </div>
                </div>
                
            );
        }

        if(canDrawAgain) {
            return (
                <div className='draw-cards'>
                    <div className='button-overlay'>
                    <Button text='Spare' clickOperation={'drawCards'} clickPayload={'1'} click={this.props.click} />
                    <Button text='Strike' clickOperation={'drawCards'} clickPayload={'2'} click={this.props.click} />
                        <ButtonGroup>
                            <Button text='+3' isGrouped={true} clickOperation={'drawCards'} clickPayload={'3'} click={this.props.click} />
                            <Button text='+4' isGrouped={true} clickOperation={'drawCards'} clickPayload={'4'} click={this.props.click} />
                            <Button text='+6' isGrouped={true} clickOperation={'drawCards'} clickPayload={'6'} click={this.props.click} />
                            <Button text='Finish' isGrouped={true} clickOperation={'finishGame'} clickPayload={null} click={this.props.click} />
                        </ButtonGroup>                        
                    </div>
                </div>
            );
        }

        return null;
    };
}

DrawCards.propTypes = {
    cardsInHand: PropTypes.number,
    cardsSelected: PropTypes.number,
    canDrawAgain: PropTypes.bool,
    click: PropTypes.func
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
