import React, { Component } from 'react';
import PropTypes from 'prop-types';
import ImmutablePropTypes from 'react-immutable-proptypes';

import { getCardinality } from '../../../helpers/getCardinality';
import { getSuit } from '../../../helpers/getSuit';
import { getSuitName } from '../../../helpers/getSuitName';

import classnames from 'classnames';
import './scoreboardRow.less';

const ScoreboardRow = ((props) => {
    
    let player = props.player;
    
    return (
        <div className='grid-x row align-center'>
        <div className='column small-2 name'>
        {player.get('name')}
        </div>
        <div className='column cards small-2'>
        {        
            player.get('cards').map((card, i) => {
                
                return (<div className={classnames('card', getSuitName(card))} key={`card-${i}`}>
                    <span>
                        {getCardinality(card)}
                        {getSuit(card)}
                    </span>
                </div>)
            })
        }
        </div>
        <div className='column small-2'>?</div>
        </div>
    );
});

ScoreboardRow.propTypes = {
    player: ImmutablePropTypes.map
};

export default ScoreboardRow;
