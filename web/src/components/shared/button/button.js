import React, { Component } from 'react';
import PropTypes from 'prop-types';
import classname from 'classnames';
import './button.less';

const Button = ((props) => {

    let {text, disabled, isGrouped} = props;
    
    if(isGrouped) {
        return (<a href='#' className='small button'><div className='inner-box'>{text}</div></a>);
    }
    
    return (<div className={classname('draw-button', disabled ? 'disabled' : null)}><a href='#' className='button'><div className='inner-box'>{text}</div></a></div>
    );
});

Button.propTypes = {
    text: PropTypes.string,
    disabled: PropTypes.bool,
    isGrouped: PropTypes.bool
};

export default Button;
