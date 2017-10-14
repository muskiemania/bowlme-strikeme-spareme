import React, { Component } from 'react';
import PropTypes from 'prop-types';
import Immutable from 'immutable';
import ImmutablePropTypes from 'react-immutable-proptypes';
import classname from 'classnames';

import './player.less'

class Player extends Component {

    render() {
	let player = this.props.player || Immutable.Map();
	let isWaiting = this.props.isWaiting;
	
	let hand = player.get('hand') || Immutable.Map();
        let name = player.get('playerName');
	let finished = player.get('finished');

	let numberOfCards = hand.get('numberOfCards') || 0;
	const cards = Immutable.List([1,2,3,4,5]);
	
        return (
            <div className='poker-table-player column'>
                <div className={classname('player-name', finished ? 'is-finished' : null)}>{ name }</div>
                <div className='player-cards'>
                    {
                        
                        cards.take(numberOfCards).map((card, i) => {
                            return <span className='player-card' key={`card-${i}`}></span>;
                        })
                    }
                    {
                        numberOfCards > 5 ? <span className='extra-cards'>{`+${numberOfCards - 5}`}</span> : null
                    }
                </div>
            </div>
        );
    }
}

Player.propTypes = {
    player: ImmutablePropTypes.map,
    isWaiting: PropTypes.bool
};

export default Player;
