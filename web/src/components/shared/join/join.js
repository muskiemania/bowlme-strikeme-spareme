import React, { Component } from 'react';
import PropTypes from 'prop-types';
import Immutable from 'immutable';
import ImmutablePropTypes from 'react-immutable-proptypes';

import './join.less';

import _ from 'lodash';
import Button from '../button/button';

class Join extends Component {

    clickJoin() {
	this.props.clickJoin(this.gameKey, this.playerName);
    }

    render() {

        return (
            <div className='join-game'>
                <div className='grid-x row align-center'>
                    <div className='column'>
                <input type='text' placeholder='Enter Your Name' ref={input => this.playerName = input} />
                    </div>
                </div>
                <div className='grid-x row align-center'>
                    <div className='column'>
                <input type='text' placeholder='Enter Game ID' ref={input => this.gameKey = input} />
                    </div>
                </div>
                <div className='grid-x row align-center'>
                    <div className='column'>
                <Button text='Join Game Now' click={this.clickJoin} />
                    </div>
                </div>
            </div>
        );
    }
}

Join.propTypes = {
    clickJoin: PropTypes.func
};

export default Join;
