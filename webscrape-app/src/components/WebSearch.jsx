import React from "react";
import '../App.css'
import search from '../assets/search.png'
import { Link } from "react-router-dom"
import axios from 'axios'
import { useContext } from "react";
import { itemsContext } from "../App.jsx"

export default function WebSearch(){
    const [items, setItems] = useContext(itemsContext)
    const [inputted, setInputted] = React.useState("")

    function clickSearch(){
        console.log("in function")
        axios.get(`http://localhost:4000/search?search=${inputted}`)
        .then(res => {
            console.log(res.data.data)
            setItems(res.data.data)
        })
        .catch(err => {
            console.log(err)
        })
    }

    return(
        <div className="search-section">
            <h2 className="ask-user">Enter a keyword</h2>
            <div className="search-bar">
                <input onChange={e => setInputted(e.target.value)} type="text" className="search-box" placeholder="E.g: fish, chicken" required></input>
                {inputted ? (
                    <Link className="link-search" to='/result' disabled={!inputted}>
                        <button type="submit" className="search-button" disabled={!inputted} onClick={clickSearch}><img className="search-image" src={search}></img></button>
                    </Link>
                ) : (
                    <button type="submit" className="search-button" disabled={true}><img className="search-image" src={search}></img></button>
                )}
            </div>
        </div>
    )
}