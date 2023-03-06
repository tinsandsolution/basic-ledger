import { useSelector, useDispatch } from 'react-redux';
import React, { useState, useEffect } from 'react';
import { getAllTransactions } from '../../store/ledger';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';

const formatDate = (complicatedDate) => {
    // 2023-03-05T20:58:23.368308Z
    const date = new Date(complicatedDate);
    const year = date.getFullYear();
    const month = date.toLocaleString('default', { month: 'long' })
    const day = date.getDate();
    return `${month} ${day}, ${year}`;
}

const clipNote = (note) => {
    if (note.length > 20) {
        return note.slice(0, 20) + "...";
    }
    return note;
}

const AllTransactionsPage = ({account_id}) => {
    const dispatch = useDispatch();
    const [isLoaded, setLoaded] = useState(false);
    const transactions = useSelector(state => state.ledger.transactions);

    useEffect(() => {
        (async() => {
            await dispatch(getAllTransactions());
            setLoaded(true);
        })();
      }, [dispatch]);

    if (!isLoaded) return <></>
    return (
        <div className='transactions'>
            <TableContainer component={Paper}>
            <Table size="small" aria-label="a dense table">
                <TableHead>
                <TableRow>
                    <TableCell align="center">ID</TableCell>
                    <TableCell align="center">Date</TableCell>
                    <TableCell align="center">Transaction Type</TableCell>
                    <TableCell align="center">Account Number</TableCell>
                    <TableCell align="center">Note</TableCell>
                    <TableCell align="center">Amount</TableCell>
                </TableRow>
                </TableHead>
                <TableBody>
                {transactions && transactions[0] !== "No transactions" && transactions.map((row) => (
                    <TableRow
                    key={row.id}
                    sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                    >
                    <TableCell component="th" scope="row">
                        {row.id}
                    </TableCell>
                    <TableCell align="center">{formatDate(row.date)}</TableCell>
                    <TableCell align="center">{row.transaction_type}</TableCell>
                    <TableCell align="center">***{row.account_number.slice(-4)}</TableCell>
                    <TableCell align="center">{clipNote(row.note)}</TableCell>
                    <TableCell align="center">{row.transaction_type === "CREDIT" ? "+" : "-"}{row.amount}</TableCell>
                    </TableRow>
                ))}
                </TableBody>
            </Table>
            </TableContainer>
        </div>
    )
}

export default AllTransactionsPage;
