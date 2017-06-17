from apistar import App, Route
import condor.dbutil as condor_db
from condor.models import (
    Bibliography,
    RankingMatrix,
    TermDocumentMatrix,
    Document
)


def get_all_rankings():
    db = condor_db.session()
    rankings = [
        {
            "eid": matrix.eid,
            "term_document_matrix_eid": matrix.term_document_matrix_eid,
            "kind": matrix.kind,
            "build_options": matrix.build_options,
            "ranking_matrix_path": matrix.ranking_matrix_path
        }
        for matrix in RankingMatrix.list(db)
    ]
    db.commit()
    return rankings


def get_ranking(eid):
    db = condor_db.session()
    ranking = RankingMatrix.find_by_eid(db, eid)
    if not ranking:
        return {
            "message": "The especified eid is not found on database"
        }
    db.commit()
    return {
        "eid": ranking.eid,
        "term_document_matrix_eid": ranking.term_document_matrix_eid,
        "kind": ranking.kind,
        "build_options": ranking.build_options,
        "ranking_matrix_path": ranking.ranking_matrix_path
    }


def get_all_bibliographies():
    raise NotImplementedError


def get_bibliography():
    raise NotImplementedError


def get_all_documents():
    raise NotImplementedError


def get_document():
    raise NotImplementedError


def get_all_matrices():
    raise NotImplementedError


def get_matrix():
    raise NotImplementedError


routes = [
    Route('/ranking', 'GET', get_all_rankings),
    Route('/ranking/{eid}', 'GET', get_ranking),
    Route('/bibliography', 'GET', get_all_bibliographies),
    Route('/bibliography/{eid}', 'GET', get_bibliography),
    Route('/document', 'GET', get_all_documents),
    Route('/document/{eid}', 'GET', get_document),
    Route('/matrix', 'GET', get_all_matrices),
    Route('/matrix/{eid}', 'GET', get_matrix)
]

app = App(routes=routes)
