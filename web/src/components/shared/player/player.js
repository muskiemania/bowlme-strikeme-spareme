import React, { Component } from 'react';
import PropTypes from 'prop-types';
import ImmutablePropTypes from 'react-immutable-proptypes';
import classname from 'classnames';

import './player.less'

class Player extends Component {

    render() {
        let {player, isWaiting} = this.props;
        
        return (
            <div className='poker-table-player column'>
                <div className={classname('player-name', player.get('finished') ? 'is-finished' : null)}>{player.get('name')}</div>
                <div className='player-cards'>
                    {
                        
                        player.get('cards').take(5).map((card, i) => {
                            return <span className='player-card' key={`card-${i}`}></span>;
                        })
                    }
                    {
                        player.get('cards').size > 5 ? <span className='extra-cards'>{`+${player.get('cards').size - 5}`}</span> : null
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
