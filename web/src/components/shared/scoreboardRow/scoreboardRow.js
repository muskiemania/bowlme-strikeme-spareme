import React, { Component } from 'react';
import PropTypes from 'prop-types';
import ImmutablePropTypes from 'react-immutable-proptypes';

import { getCardinality } from '../../../helpers/getCardinality';
import { getSuit } from '../../../helpers/getSuit';
import { getSuitName } from '../../../helpers/getSuitName';

import Immutable from 'immutable';
import classnames from 'classnames';
import './scoreboardRow.less';

const ScoreboardRow = ((props) => {
    
    let player = props.player;
    let rank = player.get('rating') && player.get('rating').get('rank') || 9999;
    let cards = player.get('hand') && player.get('hand').get('cards') || Immutable.List();
    return (
        <div className={classnames('grid-x', 'row', 'align-center', 'scoreboard-row', rank === 1 ? 'winner' : '')}>
            <div className='column small-4 name'>
                {player.get('playerName')}
            </div>
            <div className='column small-4 cards'>
                <div className='float-center'>
                    {
                        cards.concat(Immutable.List(['','','','',''])).take(5).map((card, i) => {

                            return (<div className={classnames('playing-card', getSuitName(card))} key={`card-${i}`}>
                                <span className={classnames(card === '' ? 'empty-card' : null)}>
                                    {getCardinality(card)}
                                    {getSuit(card)}
                                </span>
                            </div>)
                        })
                    }
                </div>
            </div>
            <div className='column small-5 hand-details hide'>
                {
                    player.get('rating') && player.get('rating').get('description') || ''
                }
            </div>
        </div>
    );
});

ScoreboardRow.propTypes = {
    player: ImmutablePropTypes.map
};

export default ScoreboardRow;
