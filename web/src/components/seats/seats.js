import React, { Component } from 'react';
import PropTypes from 'prop-types';
import ImmutablePropTypes from 'react-immutable-proptypes';

import Player from '../shared/player/player';

import './seats.less';

const Seats = ((props) => {

    let players = props.players;
    
    return (
        <div className='poker-table-seats grid-x row align-center'>
            {
                    players.size ? players.map((player, i) => {
                        return <Player key={`player-${i}`} player={player} />
                    }) : <Player key='player-none' isWaiting={true} />
            }
        </div>
    );

});

Seats.propTypes = {
    players: ImmutablePropTypes.list
};

export default Seats;
