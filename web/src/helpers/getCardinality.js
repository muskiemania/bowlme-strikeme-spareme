import _ from 'lodash';

export default function getCardinality(card) {
    let cardPart = card.charAt(0);

    let xlate = {};
    xlate['T'] = '=';

    let xlated = cardPart;
    if(_.includes(['A','2','3','4','5','6','7','8','9','T','J','Q','K'], cardPart)) {
        xlated = (cardPart in xlate) ? xlate[cardPart] : cardPart;
    }

    return xlated;
}
