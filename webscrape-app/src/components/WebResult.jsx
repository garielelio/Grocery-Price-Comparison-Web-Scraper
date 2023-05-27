import React from "react";
import '../App.css'

export default function WebResult({clickButton}){
    const [userSearch, setUserSearch] = React.useState('')

    return (
        <div className="filter-container">
            <button type="submit" className="back-button" onClick={clickButton}>Menu</button>

            <div className="search-bar-2">
                <input type="text" onChange={e => setUserSearch(e.target.value)} placeholder="Search item" required></input>
            </div>
        </div>
    )
}