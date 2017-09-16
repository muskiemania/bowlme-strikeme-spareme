import React, { Component } from 'react';
import PropTypes from 'prop-types';
import ImmutablePropTypes from 'react-immutable-proptypes';

import { getCardinality } from '../../../helpers/getCardinality';
import { getSuit } from '../../../helpers/getSuit';

import './scoreboardRow.less';

const ScoreboardRow = ((props) => {
    
    let player = props.player;
    
    return (
        <div className='grid-x row align-center'>
        <div className='column'>
        {player.get('name')}
        </div>
        <div className='column cards'>
        {        
            player.get('cards').map((card, i) => {
                let cardinality = card.charAt(0);
                let suit = card.charAt(1);
                
                return <div className='card' key={`card-${i}`}><Cardinality value={cardinality} /><Suit value={suit} /></div>
            })
        }
        </div>
        <div>?</div>
        </div>
    );
});

ScoreboardRow.propTypes = {
    player: ImmutablePropTypes.map
};

export default ScoreboardRow;
