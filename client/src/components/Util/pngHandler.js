import moment from 'moment';

function readPGN(pgn) {
    const pgnObj = {};

    const dateRegex = /Date "(.*)"/;
    const dateRaw = dateRegex.exec(pgn)[1];
    const yyyymmdd = dateRaw.split('.');
    const date = new Date(yyyymmdd[0], yyyymmdd[1]-1, yyyymmdd[2]);
    const formattedDate = moment(date).format('MMMM D Y');
    pgnObj['date'] = formattedDate;

    const resultRegex = /Result "(.*)"/;
    const result = resultRegex.exec(pgn)[1];
    pgnObj['result'] = result;

    const whiteUsernameRegex = /White "(.*)"/;
    const whiteUsername = whiteUsernameRegex.exec(pgn)[1];
    pgnObj['whiteUsername'] = whiteUsername;

    const blackUsernameRegex = /Black "(.*)"/;
    const blackUsername = blackUsernameRegex.exec(pgn)[1];
    pgnObj['blackUsername'] = blackUsername;

    const pgnSplit = pgn.split('\n');
    const moveListSplit = pgnSplit.slice(pgnSplit.indexOf('') + 1);
    const moveList = moveListSplit.join(' ');
    pgnObj['moveList'] = moveList;

    return pgnObj;
}

export default readPGN;