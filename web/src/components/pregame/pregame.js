import React, { Component } from 'react';
import PropTypes from 'prop-types';
import ImmutablePropTypes from 'react-immutable-proptypes';
import classname from 'classnames';

import './pregame.less';

import Button from '../shared/button/button';

export default class Pregame extends Component {

    render() {
        let {isHost, numberOfPlayers, playersRequired} = this.props;

	let hostText = 'Start Game Now';
	let disabled = false;
	if (numberOfPlayers < playersRequired) {
	    hostText = 'Waiting For Players...';
	    disabled = true;
	}
        return (
                <div className='pregame'>
                <div className={classname('button-overlay', isHost ? 'start-game' : 'waiting')}>
                <Button text={isHost ? hostText : 'Waiting For Host To Start Game'} disabled={disabled} clickOperation={'startGame'} click={isHost ? this.props.click : null} />
                </div>
                </div>               
        );
    };
}

Pregame.propTypes = {
    isHost: PropTypes.bool,
    numberOfPlayers: PropTypes.number,
    playersRequired: PropTypes.number,
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
