import React, { Component } from 'react';
import PropTypes from 'prop-types';
import ImmutablePropTypes from 'react-immutable-proptypes';

import './player.less'

const Player = ((props) => {

    let player = props.player;
    
    return (
        <div className='poker-table-player column'>
            <div>{player}</div>
            <div>* * * * *</div>
        </div>
    );

});

Player.propTypes = {
    player: PropTypes.string
};

export default Player;
