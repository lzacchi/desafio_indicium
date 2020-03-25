'''importing pandas'''
import pandas as pd
import os


def sales_per_contact(deals, contacts):
    '''This function receives 2 Pandas DataFrames
    and computes stuff'''
    grouped_deals = deals.groupby(['contactsId'])['dealsPrice'].sum()
    grouped_deals = grouped_deals.to_frame()
    grouped_deals = grouped_deals.reset_index()

    deals_per_contact = pd.merge(grouped_deals, contacts[['contactsId', 'contactsName']], on='contactsId', how='left')
    deals_per_contact = deals_per_contact[['contactsId', 'contactsName', 'dealsPrice']]
    deals_per_contact = deals_per_contact.rename(columns={'dealsPrice': 'dealsTotal'})
    deals_per_contact.to_csv('output/sales_per_contact.csv', index=False)


def montlhy_sales(deals):
    '''docstring'''
    deals['dealsMonth'] = pd.DatetimeIndex(deals['dealsDateCreated']).month
    deals['dealsYear'] = pd.DatetimeIndex(deals['dealsDateCreated']).year

    grouped_dates = deals.groupby(['dealsMonth', 'dealsYear'])['dealsPrice'].sum()
    grouped_dates = grouped_dates.to_frame()
    grouped_dates = grouped_dates.sort_values(by=['dealsYear', 'dealsMonth'])
    grouped_dates.to_csv('output/monthly_sales.csv')


def percentage_per_sector(companies, sectors, deals):
    '''docstring'''
    grouped_companies = deals.groupby(['companiesId'])['dealsPrice'].sum()

    deals_sector = pd.merge(grouped_companies,companies[['companiesId', 'sectorKey']], on='companiesId', how='left')
    deals_sector = deals_sector.reset_index()

    grouped_sector = deals_sector.groupby(['sectorKey'])['dealsPrice'].sum()

    total_by_sector = pd.merge(grouped_sector, sectors[['sectorKey', 'sector']], on='sectorKey', how='left')
    total_by_sector = total_by_sector.reset_index()
    total_by_sector = total_by_sector[['sectorKey', 'sector', 'dealsPrice']]

    total = sum(total_by_sector['dealsPrice'])
    total_by_sector['dealsPrice'] = total_by_sector['dealsPrice']/total
    total_by_sector = total_by_sector.sort_values(by=['dealsPrice'],ascending=False)

    total_by_sector.to_csv('output/percentage_per_sector.csv', index=False)



if __name__ == '__main__':

    try:
        os.stat('output')
    except:
        os.mkdir('output')

    print('reading companies.tsv')
    companies = pd.read_csv('data/companies.tsv', sep='\t')
    print('done!')
    print('reading contacts.tsv')
    contacts = pd.read_csv('data/contacts.tsv', sep='\t')
    print('done!')
    print('reading deals.tsv')
    deals = pd.read_csv('data/deals.tsv', sep='\t')
    print('done!')
    print('reading sectors.tsv')
    sectors = pd.read_csv('data/sectors.tsv', sep='\t')
    print('done!')

    deals['dealsDateCreated'] = pd.to_datetime(deals['dealsDateCreated'])

    print("Generating output files...")

    sales_per_contact(deals, contacts)
    montlhy_sales(deals)
    percentage_per_sector(companies, sectors, deals)

    print("Done! You can find the files inside the 'output' folder")
