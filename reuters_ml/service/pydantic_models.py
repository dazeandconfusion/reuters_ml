from pydantic import BaseModel


class Output(BaseModel):
    """
    Data validation output
    """

    prediction: tuple
