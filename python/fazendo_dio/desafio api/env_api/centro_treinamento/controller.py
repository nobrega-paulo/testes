from uuid import uuid4
from fastapi import APIRouter, Body, status, HTTPException
from env_api.centro_treinamento.schemas import CentrotreinamentoIn, CentroTreinamentoOut
from env_api.centro_treinamento.models import CentroTreinamentoModel
from pydantic import UUID4

from env_api.contrib.dependencies import DatabaseDependency
from sqlalchemy.future import select
router = APIRouter()


@router.post(
    '/',
    summary='Criar um novo Centro de treinamento',
    status_code=status.HTTP_201_CREATED,
    response_model=CategoriaOut,
)
async def post(
    db_session: DatabaseDependency, 
    centro_treinamento_in: CentrotreinamentoIn = Body(...)
) -> CentroTreinamentoOut:
    centro_treinamento_Out = CentroTreinamentoOut(id=uuid4(), **CentrotreinamentoIn.model_dump())
    centro_treinamento_Model = CentroTreinamentoModel(**centro_treinamento_Out.model_dump())

    db_session.add(CentroTreinamentoModel)
    await db_session.commit()
    return centro_treinamento_Out

@router.get(
    '/',
    summary='Consultar todos os centros de treinamentos',
    status_code=status.HTTP_200_OK,
    response_model=list[CentroTreinamentoOut],
)
async def query(db_session: DatabaseDependency) -> list[CentroTreinamentoOut]:
    centro_treinamento_Out: list[CentroTreinamentoOut] = (
        await db_session.execute(select(CentroTreinamentoModel))
    ).scalars().all()
    
    return centro_treinamento_Out

@router.get(
    '/{id}',
    summary='Consultar um centro de treinamento pelo id',
    status_code=status.HTTP_200_OK,
    response_model=CentroTreinamentoOut,
)
async def query(id: UUID4, db_session: DatabaseDependency) -> CentroTreinamentoOut:
    centro_treinamento_Out: CentroTreinamentoOut = (
        await db_session.execute(select(CentroTreinamentoModel).filter_by(id=id))
    ).scalars().first()
    
    if not centro_treinamento_Out:
        raise centro_treinamento_Out(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'centro de treinamento não encontrado no id: {id}'
        )
    
    return centro_treinamento_Out