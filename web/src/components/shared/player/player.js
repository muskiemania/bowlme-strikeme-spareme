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
	
	let cards = player.get('cards') || Immutable.List();
        let name = player.get('name');
	let finished = player.get('finished');
	
        return (
            <div className='poker-table-player column'>
                <div className={classname('player-name', finished ? 'is-finished' : null)}>{ name }</div>
                <div className='player-cards'>
                    {
                        
                        cards.take(5).map((card, i) => {
                            return <span className='player-card' key={`card-${i}`}></span>;
                        })
                    }
                    {
                        cards.size > 5 ? <span className='extra-cards'>{`+${cards.size - 5}`}</span> : null
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
