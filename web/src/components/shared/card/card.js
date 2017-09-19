import React, { Component } from 'react';
import PropTypes from 'prop-types';
import './card.less';
import { getCardinality } from '../../../helpers/getCardinality';
import { getSuit } from '../../../helpers/getSuit';
import { getSuitName } from '../../../helpers/getSuitName';
import classnames from 'classnames';


class Card extends Component {

    handleTouch(e){
	e.preventDefault();
        this.props.toggleSelected(this.props.card);
    }
    
    render() {
        let {card, index, isSelected} = this.props;
        
        return (
            <div className={classnames('column', 'a-card', getSuitName(card), `card-${index}`, isSelected ? 'selected' : '')} onTouchEnd={this.handleTouch.bind(this)} onClick={this.handleTouch.bind(this)}>
                <div className='cardinality'>
                    <span>
                        { getCardinality(card) }
                    </span>
                </div>
                <div className='suit'>
                    <span>
                        { getSuit(card) }
                    </span>
                </div>
                <div className='big'>
                    <div className='suit'>
                        <span>
                            { getSuit(card) }
                        </span>
                    </div>
                </div>
            </div>
        );
    }
}

Card.propTypes = {
    card: PropTypes.string,
    index: PropTypes.number,
    isSelected: PropTypes.bool,
    toggleSelected: PropTypes.func
};

export default Card;
