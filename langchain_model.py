from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain


def generate_restaurant_idea(cuisine):
    llm = OpenAI(temperature=0.6)

    pt_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to start a restaurant serving {cuisine} food. Suggest me exactly one name for it."
    )
    chain_name = LLMChain(llm=llm, prompt=pt_name)

    pt_menu = PromptTemplate(
        input_variables=['name'],
        template="Suggest some menu items for {name}"
    )
    chain_menu = LLMChain(llm=llm, prompt=pt_menu)


    chain_name = LLMChain(llm=llm, prompt=pt_name, output_key='name')
    chain_menu = LLMChain(llm=llm, prompt=pt_menu, output_key='menu')

    chain_seq = SequentialChain(
        chains = [chain_name, chain_menu],
        input_variables = ['cuisine'],
        output_variables = ['name', 'menu'],
        verbose = True
    )

    response = chain_seq.invoke({'cuisine': cuisine})
    
    return response


if __name__ == "__main__":
    print(generate_restaurant_idea("Indian"))