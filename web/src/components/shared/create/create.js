import React, { Component } from 'react';
import PropTypes from 'prop-types';
import Immutable from 'immutable';
import ImmutablePropTypes from 'react-immutable-proptypes';

import './create.less';

import _ from 'lodash';
import Button from '../button/button';

class Create extends Component {

    constructor() {
	super();
	this.state = {};
    }
    
    clickCreate() {
	this.props.clickCreate(this.state.playerName);
    }

    handleChange(text) {
	this.setState({playerName: text});
    }

    render() {

        return (
            <div className='create-game'>
                <div className='grid-x row align-center'>
                    <div className='column'>
                <input type='text' placeholder='Enter Your Name' onChange={(e) => this.handleChange(e.target.value)} />
                    </div>
                </div>
                <div className='grid-x row align-center'>
                    <div className='column'>
                <Button text='Play Now!' click={this.clickCreate.bind(this)} />
                    </div>
                </div>
            </div>
        );
    }
}

Create.propTypes = {
    clickCreate: PropTypes.func
};

export default Create;
