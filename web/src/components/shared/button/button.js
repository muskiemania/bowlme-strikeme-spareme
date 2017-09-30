import React, { Component } from 'react';
import PropTypes from 'prop-types';
import classname from 'classnames';
import './button.less';

class Button extends Component {

    handleTouchClick(e) {
	e.preventDefault();
	this.props.click();
    }
    
    render() {
    
        let {text, disabled, isGrouped} = this.props;
        
        if(isGrouped) {
            return (
                <a href='#' className='small button'>
                    <div className='inner-box'>
                        {text}
                    </div>
                </a>);
        }
    
        return (<div className={classname('draw-button', disabled ? 'disabled' : null)}>
		<a href='#' className='button' onClick={(e) => this.handleTouchClick(e)}>
                <div className='inner-box'>
                    {text}
                </div>
            </a>
        </div>
        );
    }
}

Button.propTypes = {
    text: PropTypes.string,
    disabled: PropTypes.bool,
    isGrouped: PropTypes.bool,
    click: PropTypes.func
};

export default Button;
