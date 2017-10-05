import React, { Component } from 'react';
import PropTypes from 'prop-types';
import Immutable from 'immutable';
import ImmutablePropTypes from 'react-immutable-proptypes';

import './join.less';

import _ from 'lodash';
import Button from '../button/button';

class Join extends Component {

    constructor() {
	super();
	this.state = {};
    }
    
    clickJoin() {
	this.props.clickJoin(this.state.gameKey, this.state.playerName);
    }

    handleNameChange(text) {
	this.setState({playerName: text});
    }

    handleGameChange(text) {
	this.setState({gameKey: text});
    }

    render() {
	
        return (
            <div className='join-game'>
                <div className='grid-x row align-center'>
                    <div className='column'>
                <input type='text' placeholder='Enter Your Name' onChange={(e) => this.handleNameChange(e.target.value)} />
                    </div>
                </div>
                <div className='grid-x row align-center'>
                    <div className='column'>
                <input type='text' placeholder='Enter Game ID' onChange={(e) => this.handleGameChange(e.target.value)} />
                    </div>
                </div>
                <div className='grid-x row align-center'>
                    <div className='column'>
                <Button text='Join Game Now' click={this.clickJoin.bind(this)} />
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
