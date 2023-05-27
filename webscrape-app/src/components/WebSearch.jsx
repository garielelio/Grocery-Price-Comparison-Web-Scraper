import React from "react";
import '../App.css'
import search from '../assets/search.png'

export default function WebSearch({clickButton}){

    const [inputted, setInputted] = React.useState("")

    return(
        <div className="search-section">
            <h2 className="ask-user">Enter a keyword</h2>
            <div className="search-bar">
                <input onChange={e => setInputted(e.target.value)} type="text" className="search-box" placeholder="E.g: fish, chicken" required></input>
                <button type="submit" className="search-button" onClick={clickButton} disabled={!inputted}><img className="search-image" src={search}></img></button>
            </div>
        </div>
    )
}