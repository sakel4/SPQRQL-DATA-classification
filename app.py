from flask import Flask
from RetrieveData.retrieveService import retrieveService


app = Flask(__name__)


rt = retrieveService();
    
#region #BNF
@app.route("/BNFtriplets")
def getAllBNFTriplets():
    return rt.getAllBNF();

@app.route("/types")
def getAllBNFTypes():
    return rt.getBNFtypes();

@app.route("/predicates")
def getAllBNFPredicates():
    return rt.getAllBNF();
#endregion

#region #DBpedia
@app.route("/DBPediaTriplets")
def getAllDBPediaTriplets():
    return rt.getAllDBPedia();

@app.route("/DBpediaTypes")
def getAllDBpediaTypes():
    return rt.getDBPediaTypes();

@app.route("/DBpediaPredicates")
def getAllDBpediaPredicates():
    return rt.getDBPediaPredicates();
#endregion

#region #Conference
@app.route("/ConferenceTriplets")
def getAllConferenceTriplets():
    return rt.getAllConference();

@app.route("/Conferencetypes")
def getAllConferenceTypes():
    return rt.getConferenceTypes();

@app.route("/Conferencepredicates")
def getAllConferencePredicates():
    return rt.getConferencePredicates();
#endregion

#region #HistMunic    
@app.route("/HistMunicTriplets")
def getAllHistMunicTriplets():
    return rt.getAllHistMunic();

@app.route("/HistMunicTypes")
def getAllHistMunicTypes():
    return rt.getHistMunicTypes();

@app.route("/HistMunicPredicates")
def getAllHistMunicPredicates():
    return rt.getHistMunicPredicates();
#endregion

