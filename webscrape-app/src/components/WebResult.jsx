import React from "react";
import '../App.css'
import ResultItems from "./ResultItems";
import { Link } from "react-router-dom"
import { useContext } from "react";
import { itemsContext } from "../App.jsx"

export default function WebResult(){
    const [items, setItems] = useContext(itemsContext)
    const [userSearch, setUserSearch] = React.useState('')

    const itemCards = items.map(item => {
        return (
            <ResultItems title={item.NAME} store={item.STORE} price={item.PRICE.toFixed(2)}/>
        )
    })

    return (
        <>
            <div className="filter-container">
                <Link className="Link" to='/'>
                    <button type="submit" className="back-button">Menu</button>
                </Link>

                <div className="search-bar-2">
                    <input type="text" onChange={e => setUserSearch(e.target.value)} placeholder="Search item" required></input>
                </div>
            </div>
            <div className="result-container">
                {/* <ResultItems title="Chicken Noodle Soup" store="Longos"/>
                <ResultItems title="Chicken" store="Longos"/>
                <ResultItems title="Chicken Noodle Soup" store="Longos"/>
                <ResultItems title="Chicken Noodle Soup" store="Longos"/>
                <ResultItems title="Chicken Noodle Soup" store="Longos"/>
                <ResultItems title="Chicken Noodle Soup" store="Longos"/>
                <ResultItems title="Chicken Noodle Soup" store="Longos"/> */}
                {itemCards}
            </div>
        </>
    )
}